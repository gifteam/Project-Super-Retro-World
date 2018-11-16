using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Brain
{
    public NetworkPop m_networkPop;
    public BlocPop m_blocPop;

    public Brain()
    {
        m_networkPop = new NetworkPop();
    }

    public void update()
    {
        Debug.Log("brain learn");
        m_networkPop.update();
    }

    public void evolve(float a_mRate)
    {
        Debug.Log("brain evolve");
    }
}