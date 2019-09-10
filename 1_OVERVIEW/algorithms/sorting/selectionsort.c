//OVERVIEW OF SOFTWARE DEVELOPMENT COURSE, 246
//SELECTION SORT
//example seems like it's in C#, so I'm using c

//selection sort finds the lowest element in the array
//and swaps into element[0], then it finds the next lowest
//element and swaps into element[1], and so on

//sometimes an entirely different array of the same size is
//used and each element is 'selected' and put in the element
//in the new array...this example uses the same array


#include <stdio.h>

void main() {
	
	//array to sort
	int nums[] = {5, 2, 1, 7, 6};
	unsigned int nums_length = sizeof(nums)/sizeof(nums[0]);
	
	//state
	int minPosition;
	int temp;
	
	//selection sort algorithm
	for(int counter=0; counter<nums_length-1; counter++) {
		minPosition = counter;
		for(int index=counter+1; index<nums_length; index++) {
			if(nums[index] < nums[minPosition])
				minPosition = index;
		}
		if(minPosition != counter) {
			temp = nums[counter];
			nums[counter] = nums[minPosition];
			nums[minPosition] = temp;
		}
	}
	
	//print result
	for(int i = 0; i < nums_length; i++)
		printf("%i", nums[i]);
	
}