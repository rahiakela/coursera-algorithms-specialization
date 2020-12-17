package com.bs;

public class BinarySearch {

	public static void main(String[] args) {
		int[] records = {6, 13, 14, 25, 33, 43, 51, 53, 64, 72, 84, 93, 95, 96, 97};
		System.out.println(binarySearch(records, 84));
	}
	
	public static int binarySearch(int[] a, int key) {
		int low = 0, high = a.length -1;
		
		while(low <= high) {
			// mid calculation
			int mid = low + (high - low) / 2;
			// one 3-way compare
			if (key < a[mid]) {
				high = mid - 1;
			} else if(key > a[mid]) {
				low = mid + 1;
			} else {
				return mid;
			}
		}
		return -1;
	}
}
