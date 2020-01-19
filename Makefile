# ATTENTION. Makefile ne supporte que les tabs !!!!
dbpart1: dbpart1.c
	gcc dbpart1.c -o dbpart1

dbtest: dbtest.c
	gcc dbtest.c -o dbtest

db: db.c
	gcc db.c -o db

run: db
	./db mydb.db

clean:
	rm -f db *.db

test: db
	bundle exec rspec

format: *.c
	clang-format -style=Google -i *.c