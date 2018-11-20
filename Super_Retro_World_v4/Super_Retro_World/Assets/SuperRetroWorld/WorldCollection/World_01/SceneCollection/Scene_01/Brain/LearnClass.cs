using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LearnClass : MonoBehaviour {

    public Brain m_brain;
    public bool m_showResult;
    public BlocPop m_blocs;
    public float m_mutationRate = 0.1f;

    // Use this for initialization
    void Start () {
        m_showResult = true;
        m_brain = new Brain();
    }
	
	// Update is called once per frame
	void Update () {
        if (m_brain.m_alive == true)
        {
            //calculate each network fitness
            m_brain.update();
        }
        else if (m_showResult == true)
        {
            //m_showResult = false;
            //show eahc network fitness
            m_brain.showFitness();
            m_brain = new Brain();
        }
    }
}
