#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int digital_root(int n) {

		printf("%d\n", n);
		printf("%d\n", --n);
		return --n % 9 + 1;

		/* if( n < 10 ) return n; */

		/* char* bf = malloc(sizeof(char) * 100); */
		/* sprintf(bf, "%d", n); */

		/* int sum = 0; */
		/* for( char* ch = bf; *ch != '\0'; ch++ ){ */
		/* 		sum += *ch - 48; */
		/* } */

		/* return digital_root(sum); */
}
