using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LearnClass : MonoBehaviour {

    public Brain m_brain;
    public BlocPop m_blocs;
    public float m_mutationRate = 0.1f;
    public GO target;

    // Use this for initialization
    void Start () {
        target = new GO(GameObject.Find("BrainTarget"));
        m_brain = new Brain();
        m_blocs = new BlocPop();
    }
	
	// Update is called once per frame
	void Update () {
        //update bloc values around the brain
        m_blocs.update(target.posCen());
        //test each network fitness
        m_brain.learn();
        //breed networks and perfom mutation
        m_brain.evolve(m_mutationRate);
    }
}
