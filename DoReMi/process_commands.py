import datetime
from global_constants import ERROR_CODES
from src.services.doremiservice import DoremiService

def parse_and_validate_date(date_str: str) -> datetime.datetime:
    try:
        date = datetime.datetime.strptime(date_str, '%d-%m-%Y')
        if 1900 <= date.year <= 9999 and 1 <= date.month <= 12 and 1 <= date.day <= 31:
            return date
        else:
            return None
    except ValueError:
        return None

def handle_start_subscription(start_date:datetime.datetime) -> None:
    if start_date is None:
        print(ERROR_CODES['ERR_INVALID_DATE'])
        
def handle_add_subscription(doremi: DoremiService, args: list, start_date: datetime.datetime) -> None:
    if start_date is None:
        print(ERROR_CODES['ERR_ADD_SUBS_INVALID_DATE'])
    else:
        # Process add subscription
        doremi.add_subscription(args[0], args[1], start_date)

def handle_add_topup(doremi: DoremiService, args: list, start_date: datetime.datetime) -> None:
    if start_date is None:
        print(ERROR_CODES['ERR_ADD_TOPUP_INVALID_DATE'])
    else:
        # Process add topup
        doremi.add_top_up(args[0], int(args[1]))

def process_file(file_path: str) -> None:
    doremi = DoremiService()
    start_date = None

    with open(file_path, 'r') as file:
        for line in file:
            input_line = line.strip("\n").split(' ')
            command = input_line[0]
            args = input_line[1:]

            if command == 'START_SUBSCRIPTION':
                start_date = parse_and_validate_date(args[0])
                
                handle_start_subscription(start_date)
                    
            elif command == 'ADD_SUBSCRIPTION':
                handle_add_subscription(doremi, args, start_date)

            elif command == 'ADD_TOPUP':
                handle_add_topup(doremi, args, start_date)

            elif command == 'PRINT_RENEWAL_DETAILS':
                doremi.print_subscriptions_details()
