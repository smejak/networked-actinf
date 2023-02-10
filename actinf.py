from utils import plot_beliefs

def actinf_loop(agent, env, T=10):
    obs = env.reset()

    for t in range(T):
        print(f"Time: {t}. Agent receives observation: {obs}")
        qs = agent.infer_states(obs)
        print(f"belief: {qs}")
        plot_beliefs(qs[0], title_str = f"Beliefs about its context at time {t}")
        plot_beliefs(qs[1], title_str = f"Beliefs about opponent context at time {t}")
        q_pi, efe = agent.infer_policies()
        chosen_action = agent.sample_action()
        print(f"Agent chose action: {chosen_action}") 
        
        obs = env.step(chosen_action[0])
        print(f"New state: {env.current_state}")