package strategy;

public class Navigator {
	private Strategy strategy;

	public Navigator(Strategy strategy) {
		super();
		this.setStrategy(strategy);
	}

	public Strategy getStrategy() {
		return strategy;
	}

	public void setStrategy(Strategy strategy) {
		this.strategy = strategy;
	}
	
	public void creerRoute() {
		strategy.creerRoute();
	}
}
