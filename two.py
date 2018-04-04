import Parameters as P
import Classes as Cls
import SupportTransientState as Support

# create multiple cohorts for when the drug is not available
#multiCohortNoDrug = Cls.MultiCohort(
 #   ids=range(P.NUM_SIM_COHORTS),   # [0, 1, 2 ..., NUM_SIM_COHORTS-1]
  #  pop_sizes=[P.REAL_POP_SIZE] * P.NUM_SIM_COHORTS,  # [REAL_POP_SIZE, REAL_POP_SIZE, ..., REAL_POP_SIZE]
   # mortality_probs=[P.MORTALITY_PROB]*P.NUM_SIM_COHORTS  # [p, p, ...]
#)
multiCohortFair=Cls.MultipleGameSets(ids=range(P.N_Games),prob_head=P.Fair_Prob, n_games_in_a_set=P.Trans_Pop_Size)




# simulate all cohorts
#multiCohortNoDrug.simulate(P.TIME_STEPS)
multiCohortFair.simulation()



# create multiple cohorts for when the drug is available
#multiCohortWithDrug = Cls.MultiCohort(
 #   ids=range(P.NUM_SIM_COHORTS, 2*P.NUM_SIM_COHORTS),   # [NUM_SIM_COHORTS, NUM_SIM_COHORTS+1, NUM_SIM_COHORTS+2, ...]
  #  pop_sizes=[P.REAL_POP_SIZE] * P.NUM_SIM_COHORTS,  # [REAL_POP_SIZE, REAL_POP_SIZE, ..., REAL_POP_SIZE]
   # mortality_probs=[P.MORTALITY_PROB*P.DRUG_EFFECT_RATIO]*P.NUM_SIM_COHORTS)


multiCohortUnfair=Cls.MultipleGameSets(ids=range(P.N_Games, 2*P.N_Games),prob_head=P.Unfair_Prob, n_games_in_a_set=P.Trans_Pop_Size)


# simulate all cohorts
#multiCohortWithDrug.simulate(P.TIME_STEPS)
multiCohortUnfair.simulation()

# print outcomes of each cohort
Support.print_outcomes(multiCohortFair, 'When drug is fair:')
Support.print_outcomes(multiCohortUnfair, 'When drug is not fair:')


# print comparative outcomes
Support.print_comparative_outcomes(multiCohortUnfair,multiCohortFair)
