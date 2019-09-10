//OVERVIEW OF SOFTWARE DEVELOPMENT COURSE, 243
//INSERTION SORT
//example seems like it's in C#, so I'm using c

//insertion sort starts further in the array each
//iteration and traverses backwards, swapping lower
//values into lower elements

//because it starts further each iteration, it seems more
//efficient than a brute force bubble sort

#include <stdio.h>

void main() {
	
	//array to sort
	int nums[] = {5, 2, 1, 7, 6};
	unsigned int nums_length = sizeof(nums)/sizeof(nums[0]);
	
	//insertion sort algorithm
	for(int counter = 0; counter < nums_length - 1; counter ++) {
		for(int index = counter + 1; index > 0; index --) {
			if(nums[index-1] > nums[index]) {
				int temp = nums[index-1];
				nums[index-1] = nums[index];
				nums[index] = temp;
			}
		}
	}
	
	//output array to stdout
	for(int i=0; i<nums_length; i++)
		printf("%i", nums[i]);
	
}