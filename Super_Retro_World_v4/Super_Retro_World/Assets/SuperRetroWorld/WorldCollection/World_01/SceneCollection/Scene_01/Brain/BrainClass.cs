using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Brain
{
    public NetworkPop m_networkPop;
    public NetworkPop m_networkPopPreviousGen;
    public bool m_alive;
    public int m_popSize = 100;

    public Brain()
    {
        m_networkPop = new NetworkPop(m_popSize);
        m_alive = true;
    }

    public Brain(NetworkPop a_networkPop)
    {
        m_networkPopPreviousGen = a_networkPop;
        m_networkPop = new NetworkPop(m_popSize);
        m_alive = true;
        crossNetworks();
    }

    public void crossNetworks()
    {
        //sort fitness
        double l_bestFitness = 1;

        foreach (Network n in m_networkPopPreviousGen.m_Networklist)
        {
            n.m_fitness = n.m_fitness * n.m_distanceRun;
        }

        foreach (Network n in m_networkPopPreviousGen.m_Networklist)
        {
            if (n.m_fitness > l_bestFitness)
            {
                l_bestFitness = n.m_fitness;
            }
        }

        List<int> l_NetworkIndexed = new List<int>();
        foreach (Network n in m_networkPopPreviousGen.m_Networklist)
        {
            int l_fitnessRatio = (int) ((n.m_fitness / l_bestFitness) * 100);
            for (int i_ratio = 0; i_ratio < l_fitnessRatio; i_ratio++)
            {
                l_NetworkIndexed.Add(n.m_index);
            }
        }

        //get 2 parents
        foreach (Network n in m_networkPop.m_Networklist)
        {
            int l_indexParentA = l_NetworkIndexed[Random.Range(0, l_NetworkIndexed.Count - 1)];
            int l_indexParentB = l_NetworkIndexed[Random.Range(0, l_NetworkIndexed.Count - 1)];

            Network l_parentA = m_networkPopPreviousGen.m_Networklist[l_indexParentA];
            Network l_parentB = m_networkPopPreviousGen.m_Networklist[l_indexParentB];
            Network l_parent;

            int l_perceptronPop = l_parentA.m_PerceptronList.Count;
            int l_midPoint = (int) Random.Range(0, l_perceptronPop - 1);

            for (int i_perceptronIndex = 0; i_perceptronIndex < l_perceptronPop; i_perceptronIndex++)
            {
                if (i_perceptronIndex < l_midPoint)
                {
                    l_parent = l_parentA;
                }
                else
                {
                    l_parent = l_parentB;
                }
                n.setWeigth(i_perceptronIndex, l_parent.m_PerceptronList[i_perceptronIndex]);
            }
        }
    }

    public void update()
    {
        //Debug.Log("brain update");
        m_networkPop.update();
        m_alive = m_networkPop.m_alive;
    }

    public void evolve(float a_mRate)
    {
       // Debug.Log("brain evolve");
    }

    public void showFitness()
    {
        string l_fitnessConcat = "";
        foreach(float i_fitness in m_networkPop.m_fitness)
        {
            l_fitnessConcat += i_fitness + ";";
        }
        Debug.Log(l_fitnessConcat);
    }

    public void showDna()
    {
        m_networkPop.getDna();
        string l_DnaConcat = "";
        foreach (List<List<double>> i_dnaPop in m_networkPop.m_dna)
        {
            foreach (List<double> i_dna in i_dnaPop)
            {
                foreach (double i_dnaPart in i_dna)
                {
                    l_DnaConcat += i_dnaPart + ";";
                }
            }
        }
        Debug.Log(l_DnaConcat);
    }
}