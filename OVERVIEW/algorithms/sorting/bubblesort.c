//OVERVIEW OF SOFTWARE DEVELOPMENT COURSE, 249
//BUBBLE SORT
//example seems like it's in C#, so I'm using c

//bubble sort seems like a brute force approach,
//it traverses the entire array for each element
//and swaps with neighbors when appropriate

#include <stdio.h>

void main() {
	
	//array to sort
	int nums[] = {5, 2, 1, 7, 6};
	unsigned int nums_length = sizeof(nums)/sizeof(nums[0]);
	
	//state
	int temp;
	
	//bubble sort algorithm
	for(int counter=0; counter<nums_length; counter++) {
		for(int index=0; index<nums_length-1; index++) {
			if(nums[index] > nums[index+1]) {
				temp = nums[index+1];
				nums[index+1] = nums[index];
				nums[index] = temp;
			}
		}
	}
	
	//print output
	for(int i = 0; i < nums_length; i++)
		printf("%i", nums[i]);
	
}