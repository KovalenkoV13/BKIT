Feature: testing bot
	Scenario: start bot
		Given I send bot message /start
		When I send bot first message /go