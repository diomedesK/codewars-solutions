#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>


/* what?
int X(char*i){return*i?*i^X(i+1)&1:0;}
*/

bool X (const char *bitstring){
		int MAX_BUFFER_SZ = 1000;

		int* parsed_numbers = malloc(sizeof(int) * MAX_BUFFER_SZ);
		int numbers_sz = 0;

		for( int i = 0; i < strlen(bitstring); i++ ){
				if( bitstring[i] == ' ' ) continue;
				char ch = bitstring[i];

				parsed_numbers[numbers_sz] = ch - 48;
				numbers_sz++;
		}

		if(numbers_sz %2 != 0){
				numbers_sz++;
				parsed_numbers[numbers_sz] = 0;
		};

		parsed_numbers = realloc(parsed_numbers, numbers_sz * sizeof(int));

		int subarrl = numbers_sz;

		while( subarrl != 1 ){
				for( int i = 0; i < ceil((double)subarrl/2); i++ ){
						int a = parsed_numbers[2*i];
						int b = parsed_numbers[2*i+1];

						parsed_numbers[i] = a ^ b;
				}

				subarrl = ceil((double)subarrl/2);
				parsed_numbers[subarrl] = 0;
		}
		return parsed_numbers[0];
}
