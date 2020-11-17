package com.basic.stack;

import java.util.Iterator;
import java.util.Scanner;

public class Stack<Item> implements Iterable<Item> {
	
	private Node first;     // top of stack (most recently added node)
	private int N;          // number of items
	
	private class Node {
		Item item;    // nested class to define nodes
		Node next;
	}
	
	public boolean isEmpty() {
		return first == null;
	}
	
	public int size() {
		return N;
	}
	
	public void push(Item item) {
		// Add item to top of stack.
		Node oldfirst = first;
		first = new Node();
		first.item = item;
		first.next = oldfirst;
		N++;
	}
	
	public Item pop() {
		// Remove item from top of stack.
		Item item = first.item;
		first = first.next;
		N--;
		
		return item;
	}
	
	public Iterator<Item> iterator() {
		return new ListIterator();
	}
	
	public class ListIterator implements Iterator<Item> {
		private Node current = first;
		
		public boolean hasNext() {
			return current != null;
		}
		
		public Item next() {
			Item item = current.item;
			current = current.next;
			return item;
		}
		
		public void remove() {}
		
	}
	
	public static void main(String[] args) {
		// Create a stack and push/pop strings as directed on StdIn.
		Stack<String> s = new Stack<String>();
		Scanner sc = new Scanner(System.in);
		while(!sc.hasNext()) {
			String item = sc.next();
			if(!item.equals("-")) {
				s.push(item);
			} else if(!s.isEmpty()) {
				System.out.println(s.pop() + " ");
			}
		}
		System.out.println("(" + s.size() + "left on stack)");
	}
}
