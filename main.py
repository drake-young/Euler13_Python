from timeit import default_timer

# ===========================================================
# PROBLEM 13 -- Large Sum
# ===========================================================
#
#  Work out the first ten digits of the sum of the following
#  one-hundred 50-digit number
#  (provided in "Problem13_Numbers.txt")
#
# ===========================================================
def problem_13( ):
    # Print Problem Context
    print( "Project Euler Problem 13 -- Large Sum" )

    # Start Timer
    start_time  =  default_timer( )

    # Retrieve and Prepare data from file
    file  =  open( "Problem13_Numbers.txt" , 'r' )
    nums  =  file.read( ).split( )
    file.close( )

    # Calculate Result
    big_sum           =  sum( int( x ) for x in nums )
    first_ten_digits  =  str( big_sum )[ 0 : 10 ]

    # Calculate Execution Time
    end_time = default_timer( )
    execution_time  =  ( end_time - start_time ) * 1000

    # Display Results
    print( "   First Ten Digits of Sum:   %s"      %  first_ten_digits )
    print( "   Computation Time:          %.3fms"  %  execution_time )
    return

if __name__ == '__main__':
    problem_13( )