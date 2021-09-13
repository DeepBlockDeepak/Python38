/* C program for Merge Sort */
#include <stdio.h> 
#include <stdlib.h> 

// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int left_index, int middle_index, int right_index) 
{ 
	int i, j, k; 
	int n1 = middle_index - left_index + 1; 
	int n2 = right_index - middle_index; 

	/* create temp arrays */
	int L[n1], R[n2]; 

	/* Copy data to temp arrays L[] and R[] */
	for (i = 0; i < n1; i++) 
		L[i] = arr[left_index + i]; 
	for (j = 0; j < n2; j++)
		//corrected Jordan Medina 09/30/2020
		R[j] = arr[middle_index + j + 1]; 
		//R[j] = arr[m + j];

	/* Merge the temp arrays back into arr[l..r]*/
	i = 0; // Initial index of first subarray 
	j = 0; // Initial index of second subarray 
	k = left_index; // Initial index of merged subarray 
	while (i < n1 && j < n2) { 
		if (L[i] <= R[j]) { 
			arr[k] = L[i]; 
			i++; 
		} 
		else { 
			arr[k] = R[j]; 
			j++; 
		} 
		k++; 
	} 

	/* Copy the remaining elements of L[], if there 
	are any */
	while (i < n1) { 
		arr[k] = L[i]; 
		i++; 
		k++; 
	} 

	/* Copy the remaining elements of R[], if there 
	are any */
	while (j < n2) { 
		arr[k] = R[j]; 
		j++; 
		k++; 
	} 
} 

/* l is for left index and r is right index of the 
sub-array of arr to be sorted */
void mergeSort(int arr[], int left_index, int right_index) 
{ 
	if (left_index < right_index) { 
		// Same as (l+r)/2, but avoids overflow for 
		// large l and h 
		int middle_ind = left_index + (right_index - left_index) / 2; 

		// Sort first and second halves 
		mergeSort(arr, left_index, middle_ind); 
		mergeSort(arr, middle_ind + 1, right_index); 

		merge(arr, left_index, middle_ind, right_index); 
	} 
} 

/* UTILITY FUNCTIONS */
/* Function to print an array */
void printArray(int A[], int size) 
{ 
	int i; 
	for (i = 0; i < size; i++) 
		printf("%d ", A[i]); 
	printf("\n"); 
} 

/* Driver program to test above functions */
int main() 
{ 
	int arr[] = { 12, 11, 13, 5, 6, 7 }; 
	int arr_size = sizeof(arr) / sizeof(arr[0]); 

	printf("Given array is \n"); 
	printArray(arr, arr_size); 

	mergeSort(arr, 0, arr_size - 1); 

	printf("\nSorted array is \n"); 
	printArray(arr, arr_size); 
	return 0; 
} 