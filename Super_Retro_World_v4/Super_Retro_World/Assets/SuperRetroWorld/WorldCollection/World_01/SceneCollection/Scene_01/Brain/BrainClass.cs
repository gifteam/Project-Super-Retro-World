using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Brain
{
    public NetworkPop m_networkPop;
    public BlocPop m_blocPop;
    public bool m_alive;

    public Brain()
    {
        m_networkPop = new NetworkPop(1);
        m_alive = true;
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