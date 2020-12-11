with open("input.txt", "r") as f:
    f = f.readlines()
    f = [line.strip("\n") for line in f]

#FIRST HALF

def check_seats(seats, row, col, row_len):
    seats_to_check = ((row-1, col-1), (row-1, col), (row-1, col+1),
                (row, col-1), (row, col+1),
                (row+1, col-1), (row+1, col), (row+1, col+1))
    count=0
    for nrow, ncol in seats_to_check:
        if nrow>=0 and nrow<len(seats) and ncol>=0 and ncol<row_len:
                if seats[nrow][ncol] == "#":
                    count+=1

    return count

def model_seats(seats):
    new_seats = []
    total = 0
    for row in range(len(seats)):
        new_row = []
        for col in range(len(seats[row])):
            seat = seats[row][col]
            if seat == "L":
                if check_seats(seats, row, col, len(seats[row])) == 0:
                    new_row.append("#")
                    total+=1
                    continue
            
            elif seat == "#":
                if check_seats(seats, row, col, len(seats[row])) >= 4:
                    new_row.append("L")
                    continue
                else:
                    total+=1
                
            new_row.append(seat)

        new_seats.append(new_row)
    
    return (new_seats, total)

new_seats, total = model_seats(f)
for x in range(500):
    new_seats, total = model_seats(new_seats)
    print(total)

#SECOND HALF

def check_seats(seats, row, col, row_len):
    seats_to_check = ((-1, -1), (-1, 0), (-1, 1),
                (0, -1), (0, 1),
                (1, -1), (1, 0), (1, 1))

    count=0
    for nrow, ncol in seats_to_check:
        dr = row+nrow
        dc = col+ncol
        while dr>=0 and dr<len(seats) and dc>=0 and dc<row_len and seats[dr][dc] == ".":
            dr += nrow
            dc += ncol

        if dr>=0 and dr<len(seats) and dc>=0 and dc<row_len:
            if seats[dr][dc] == "#":
                count+=1

    return count

def model_seats(seats):
    new_seats = []
    total = 0
    for row in range(len(seats)):
        new_row = []
        for col in range(len(seats[row])):
            seat = seats[row][col]
            if seat == "L":
                if check_seats(seats, row, col, len(seats[row])) == 0:
                    new_row.append("#")
                    total+=1
                    continue
            
            elif seat == "#":
                if check_seats(seats, row, col, len(seats[row])) >= 5:
                    new_row.append("L")
                    continue
                else:
                    total+=1
                
            new_row.append(seat)

        new_seats.append(new_row)
    
    return (new_seats, total)

new_seats, total = model_seats(f)
for x in range(100):
    new_seats, total = model_seats(new_seats)
    print(total)