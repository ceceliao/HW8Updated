import Parameters as P
import Classes as Cls
import SupportSteadyState as Support


# create a cohort of patients for when the drug is not available


cohortFair=Cls.SetOfGames(id=1,n_games=P.N_Games, prob_head=P.Fair_Prob)


# simulate the cohort
#noDrugOutcome = cohortNoDrug.simulate(P.TIME_STEPS)

FairCoinOutcome=cohortFair.simulation()


# create a cohort of patients for when the drug is available

cohortUnfair = Cls.SetOfGames(id=2,n_games=P.N_Games, prob_head=P.Unfair_Prob)


# simulate the cohort
#withDrugOutcome = cohortWithDrug.simulate(P.TIME_STEPS)
UnfairCoinOutcome=cohortUnfair.simulation()

# print outcomes of each cohort
Support.print_outcomes(FairCoinOutcome, 'When game is fair:')
Support.print_outcomes(UnfairCoinOutcome, 'When game is unfair:')



# print comparative outcomes
Support.print_comparative_outcomes(UnfairCoinOutcome, FairCoinOutcome )
