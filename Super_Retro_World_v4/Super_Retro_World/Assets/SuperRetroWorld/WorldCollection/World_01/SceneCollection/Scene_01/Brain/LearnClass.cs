using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LearnClass : MonoBehaviour {

    public Brain m_brain;
    public bool m_showResult;
    public BlocPop m_blocs;
    public int m_generationIndex = 0;
    public int m_generationMax;

    // Use this for initialization
    void Start () {
        m_generationMax = 20;
        Debug.Log("Generation " + (m_generationIndex) + " (max = " + m_generationMax + ")");
        m_showResult = true;
        m_brain = new Brain();
    }
	
	// Update is called once per frame
	void Update () {
        if (m_generationIndex < m_generationMax)
        {
            if (m_brain.m_alive == true)
            {
                //calculate each network fitness
                m_brain.update();
            }
            else
            {
                // update generation
                Debug.Log("From generation " + (m_generationIndex) + " to " + (m_generationIndex + 1) + " (max = " + m_generationMax + ")");
                m_brain = new Brain(m_brain.m_networkPop);
                m_generationIndex++;
            }
        }
    }
}
