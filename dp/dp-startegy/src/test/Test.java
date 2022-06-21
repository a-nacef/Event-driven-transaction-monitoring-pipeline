package test;

import strategy.MaxMonumentsStratgy;
import strategy.MinCoutStrategy;
import strategy.Navigator;
/*
 * Client
 */
public class Test {

	public static void main(String[] args) {
		Navigator nav = new Navigator(new MinCoutStrategy());
		
		nav.creerRoute();
		
		
		nav.setStrategy(new MaxMonumentsStratgy());

	}

}
