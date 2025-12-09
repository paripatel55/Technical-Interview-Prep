'''
Hotel Room Booking System
You are implementing the backend for a hotel booking 
platform called StayEase. The system manages hotel room bookings, 
cancellations, and availability queries. Multiple users can book 
rooms, but rooms cannot be double-booked.

Please read the entire prompt before coding. Some test cases 
will not pass unless all constraints are met.

System Overview
StayEase has hotels with rooms that can be booked by users. 
Each booking has check-in and check-out dates. Rooms cannot be 
booked if they overlap with existing bookings.

Commands
All commands are strings. Execute them in chronological order 
(by timestamp), but return results in input order.

1. ADD_HOTEL
text
ADD_HOTEL, hotel_id, room_count
Adds a new hotel with a number of identical rooms.

hotel_id: Unique string identifier

room_count: Integer 1-100 (number of identical rooms)

Rules:

If hotel already exists → "FAILURE"

Otherwise → "SUCCESS"

2. BOOK_ROOM
text
BOOK_ROOM, timestamp, user_id, hotel_id, check_in_date, 
check_out_date
Attempts to book a room at a hotel for specific dates.

Dates are integers (day numbers, e.g., 1, 5, 10)

check_out_date must be > check_in_date

Booking Rules:

If hotel doesn't exist → "FAILURE"

If dates are invalid (check_out ≤ check_in) → "FAILURE"

If no room available for those dates → "FAILURE"

Otherwise → "SUCCESS" and:

Mark a room as booked for those dates

Booking is assigned to smallest available room number

3. CANCEL_BOOKING
text
CANCEL_BOOKING, timestamp, user_id, hotel_id, check_in_date
Cancels an existing booking.

Identified by user_id, hotel_id, and check_in_date (unique per user-hotel)

Rules:

If booking doesn't exist → "FAILURE"

If check_in_date is in the past relative to timestamp → "FAILURE" 
(can't cancel past stays)

Otherwise → "SUCCESS" and free the room

4. CHECK_AVAILABILITY
text
CHECK_AVAILABILITY, timestamp, hotel_id, date
Returns number of rooms available at a hotel on a specific date.

If hotel doesn't exist → "FAILURE"

Otherwise → integer count of available rooms

Important Notes
Rooms are numbered 1 to room_count

Each room maintains its own booking calendar

Booking overlap means: new_check_in < existing_check_out AND 
new_check_out > existing_check_in

One user can have multiple bookings at same/different hotels

Users cannot book more than one room at the same hotel for 
overlapping dates

All timestamps are unique within input

Dates are relative (e.g., day 1, day 5), not real dates

Input/Output Format
Input: List of command strings
Output: Comma-separated results in input order

Example:

text
Input:
[
  "ADD_HOTEL, H1, 3",
  "BOOK_ROOM, 2, U1, H1, 5, 10",
  "CHECK_AVAILABILITY, 3, H1, 6",
  "BOOK_ROOM, 4, U2, H1, 8, 12"
]

Process order by timestamp: ADD(no timestamp=0), BOOK@2, CHECK@3, 
BOOK@4
Output order (input): SUCCESS, SUCCESS, 2, FAILURE

Explanation:
- Room booked days 5-10 (exclusive end)
- On day 6: 2 rooms left (3 total, 1 booked)
- Second booking fails (overlaps with first: 8 < 10)
Constraints
Maximum 50 hotels, 1000 rooms total

Dates: 1-365

Timestamps: positive integers

User IDs: alphanumeric

At most one command per timestamp

This prompt has:

Similar length and complexity to your original

Multiple command types with specific rules

Timestamp ordering requirement

State management (bookings, availability)

Input/output format constraints

Clear example at the end

Practice breaking this down using our 5-step framework.

'''

'''
Key takeaways: 
Input: list of command strings
Output: results in input order
- main goal to book hotel rooms for users 
- need to timestamp when room booked 
- sort by timestamp but return in og output (need to track og index)

commands: 
add_hotel
- init hotel and roomcount
- hotel already exists -> failture
output: success or failture

bookroom: 
- book hotel + room, check date and time 
- check out date > check in date else failture
- hotel doesnt exist -> failture
- if successs mark room booked -> assigned to smallest rn

cancelbooking
- hotel doesnt exist -> failture
- rooms mapped to booking calender 
- 
check avalible

'''