import streamlit as st
import numpy as np
from CodeSnippets import SIMPLE_BANDIT_ALG

def run():
    st.write("## Pseudocode and Implementations")
    st.write("""
             This Section contains pseudocode from the Book and simple NumPy implementations thereof.
             """)
    st.write("### A simple bandit algorithm (Chapter 2.4)")
    
    with st.expander("See Pseudocode:"):
            
        st.text(r"""
                Initialize, for a = 1 to k:
                    Q(a) <- 0
                    N(a) <- 0 
                    
                Loop forever: 
                    With probability 1 - ε: 
                        A <- argmax_a Q(a) 
                    Else (with probability ε):
                        A <- a random action 
                        
                    R    <- bandit(A)
                    N(A) <- N(A) + 1 
                    Q(A) <- Q(A) + 1/N(A)[R - Q(A)]
                """)
        
        # st.image('Chapters\simple_bandit_alg.png')
    
    with st.expander("See NumPy implementation:"):
        st.code(SIMPLE_BANDIT_ALG, language="python")

action_space = [0,1,2,3]
epsilon = 0.05

def bandit_algorithm(action, epsilon):
    bandit = np.random.randn(len(action_space))
    Q = np.zeros(len(action_space))
    N = np.zeros(len(action_space))
    
    finished = False 
    
    while finished:
        if np.random.rand() < 1- epsilon:
            action = np.argmax(Q)
        else:
            np.random.choice(action_space)
        reward = bandit(action)
        N[action] = N[action] + 1
        Q[action] = Q[action] + 1/N[action] * (reward - Q[action])