package com.stack;

// Stack: array implementation
public class FixedCapacityStackOfStrings {
	
	private String[] s;
	private int N = 0;
	
	public FixedCapacityStackOfStrings(int capacity) {
		s = new String[capacity];
	}
	
	public boolean isEmpty() {
		return N == 0;
	}
	
	public void push(String item) {
		s[N++] = item;
	}
	
	public String pop() {
		// loitering problem
		// return s[--N];
		
		// Loitering. Holding a reference to an object when it is no longer needed.
		String item = s[--N];
		s[N] = null;
		return item;
	}
}
