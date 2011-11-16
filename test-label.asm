MOV A,#00
MOV r2,#10
again: add a,#03
djnz r2,again
MOV R5,A
sjmp sam
mov r1,#05
sam: mov r6,#34
