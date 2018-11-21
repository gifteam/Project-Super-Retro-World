using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LearnClass : MonoBehaviour {

    public Brain m_brain;
    public bool m_showResult;
    public BlocPop m_blocs;
    public float m_mutationRate = 0.1f;
    public int m_brainPop = 10;
    public int m_brainIndex = 0;
    public int m_generationIndex = 0;
    public int m_generationMax = 10;

    // Use this for initialization
    void Start () {
        m_showResult = true;
        m_brain = new Brain();
    }
	
	// Update is called once per frame
	void Update () {
        if (m_brainIndex < m_brainPop)
        {
            if (m_brain.m_alive == true)
            {
                //calculate each network fitness
                m_brain.update();
            }
            else if (m_showResult == true)
            {
                //m_brain.showFitness();
                //m_brain.showDna();
                Debug.Log("Generation " + m_generationIndex + " : from brain " + (m_brainIndex) + " to " + (m_brainIndex + 1) + " (popSize =  " + m_brainPop + ")");
                m_brain = new Brain();
                m_brainIndex++;
            }
        }
        else
        {
            if (m_generationIndex < m_generationMax)
            {
                Debug.Log("From generation " + (m_generationIndex) + " to " + (m_generationIndex + 1) + "(max = " + m_generationMax + ")");
                m_brainIndex = 0;
                m_generationIndex++;
            }
        }
    }
}
