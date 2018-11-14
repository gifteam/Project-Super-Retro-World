using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NetworkPop
{
    public int m_pop;
    public List<Network> m_Networklist;

    public NetworkPop()
    {
        m_Networklist = new List<Network>();
        m_pop = 100;
        for (uint i_popIndex = 0; i_popIndex < m_pop; i_popIndex++)
        {
            m_Networklist.Add(new Network());
        }
    }
}

public class Network
{
    public float m_fitness;
    public List<Perceptron> m_PerceptronList;

    public Network()
    {
        m_PerceptronList = new List<Perceptron>();
        m_fitness = 0;
        uint l_pop = (uint)Mathf.RoundToInt(Random.Range(0.0f, 1.0f));
        for (uint i_popIndex = 0; i_popIndex < l_pop; i_popIndex++)
        {
            m_PerceptronList.Add(new Perceptron());
        }
    }
}
