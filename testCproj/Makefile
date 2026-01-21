CC=gcc
CCFLAGS=-std=c17 -Wall -g
TARGET=run
SRCS=main.c $(wildcard lib/*.c)
OBJS=$(SRCS:.c=.o)

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(CCFLAGS) $(OBJS) -o $(TARGET)

%.o: %.c
	$(CC) $(CCFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS) $(TARGET)