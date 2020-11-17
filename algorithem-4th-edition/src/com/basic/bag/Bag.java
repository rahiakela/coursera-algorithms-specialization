package com.basic.bag;

import java.util.Iterator;

public class Bag<Item> implements Iterable<Item> {
	
	private Node first;     // first node in list
	
	private class Node{
		Item item;
		Node next;
	}
	
	public void add(Item item) {
		Node oldfirst = first;
		first = new Node();
		first.item = item;
		first.next = oldfirst;
	}
	
	public Iterator<Item> iterator() {
		return new ListIterator();
	}
	
	private class ListIterator implements Iterator<Item> {
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
}
