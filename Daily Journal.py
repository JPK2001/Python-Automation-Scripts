import datetime

def today ():
    current_date = datetime.datetime.now ( ).strftime ( "%Y-%m-%d" )
    beginning_time = input ( "Enter the beginning time of the day (HH:MM AM/PM): " )
    end_time = input ( "Enter the end time of the day (HH:MM AM/PM): " )
    summary = input ( "Daily report: \n" )

    # Format the summary with date, beginning time, and end time
    formatted_summary = f"Date: {current_date}\nBeginning Time: {beginning_time}\nEnd Time: {end_time}\n\n{summary}\n\n"

    # Append the summary to the journal file
    with open ( 'MyJournal.txt', 'a' ) as file:
        file.write ( formatted_summary )


today ( )
