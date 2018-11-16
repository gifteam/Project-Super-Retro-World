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
        m_pop = 3;
        for (uint i_popIndex = 0; i_popIndex < m_pop; i_popIndex++)
      {
            m_Networklist.Add(new Network());
        }  
    }

    public void update()
    {
        foreach (Network n in m_Networklist)
        {
            n.update();
        }
    }
}

public class Network
{
    public float m_fitness;
    public List<Perceptron> m_PerceptronList;
    public BlocPop m_blocPop;
    public Control m_control;
    public GO m_target;
    public GO m_targetParent;
    public GO m_targetOriginal;

    public Network()
    {
        m_control = new Control();
        m_targetParent = new GO(GameObject.Find("MachineLearning"));
        m_targetOriginal =new GO(GameObject.Find("Geko"));
        m_target = new GO(GameObject.Instantiate(m_targetOriginal.getGO().transform, m_targetParent.getGO().transform).gameObject);
        m_blocPop = new BlocPop(m_target);
        m_PerceptronList = new List<Perceptron>();
        m_fitness = 0;
        uint l_pop = (uint)Mathf.RoundToInt(Random.Range(0.0f, 1.0f));
        for (uint i_popIndex = 0; i_popIndex < l_pop; i_popIndex++)
        {
            m_PerceptronList.Add(new Perceptron(m_blocPop, m_control));
        }
    }

    public void update()
    {
        m_blocPop.update();
        foreach (Perceptron p in m_PerceptronList)
        {
            p.update();
        }
    }
}
