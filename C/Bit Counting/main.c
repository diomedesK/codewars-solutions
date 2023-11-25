#include <stddef.h>

size_t countBits(unsigned value){
		int count = 0;
		for( ; value != 0 ;  ){
				count += value % 2;
				value /= 2;
		}

		return count;
}
