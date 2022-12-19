"""
Prisoners Dilemma game using PyCID.
Follows the following notebook: 
https://colab.research.google.com/github/causalincentives/pycid/blob/master/notebooks/MACID_Basics_Tutorial.ipynb
"""
import pycid
import numpy as np
# import dataclass



if __name__ == "__main__":
    macid = pycid.MACID(
        [("D1", "U1"), ("D1", "U2"), ("D2", "U1"), ("D2", "U2")],
        agent_decisions={1: ["D1"], 2: ["D2"]},
        agent_utilities={1: ["U1"], 2: ["U2"]},
    )

    # Specify domains
    d1_domain = ["C", "D"]
    d2_domain = ["C", "D"]

    # normal form matrix for player 1
    player1_payoff = np.array(
        [[-1, -3], [0, -2],]  # Cooperate payoffs  # Defect payoffs
    )
    player2_payoff = np.transpose(player1_payoff)

    # not very well documented (what is CPDS?)
    macid.add_cpds(
        D1 = d1_domain,
        D2 = d2_domain,
        U1 = lambda D1, D2: player1_payoff[d1_domain.index(D1), d2_domain.index(D2)],
        U2 = lambda D1, D2: player2_payoff[d1_domain.index(D1), d2_domain.index(D2)],
    )

    macid.draw()

