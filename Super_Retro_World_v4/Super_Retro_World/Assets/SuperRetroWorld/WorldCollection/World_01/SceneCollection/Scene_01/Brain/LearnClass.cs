using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LearnClass : MonoBehaviour {

    public Brain m_brain;
    public BlocPop m_blocs;
    public float m_mutationRate = 0.1f;

    // Use this for initialization
    void Start () {
        m_brain = new Brain();
    }
	
	// Update is called once per frame
	void Update () {
        //test each network fitness
        m_brain.update();
        //breed networks and perfom mutation
        m_brain.evolve(m_mutationRate);
    }
}
