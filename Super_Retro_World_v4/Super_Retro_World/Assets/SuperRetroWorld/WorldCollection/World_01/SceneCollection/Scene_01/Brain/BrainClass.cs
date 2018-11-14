using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Brain
{
    public NetworkPop m_networkPop;

    public Brain()
        {
        m_networkPop = new NetworkPop();
        }

    public void learn()
    {
        Debug.Log("brain learn");
    }

    public void evolve(float a_mRate)
    {
        Debug.Log("brain evolve");
    }
}