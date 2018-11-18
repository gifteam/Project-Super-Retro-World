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
        m_pop = 1;
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
    public Rigidbody2D m_targetBody;
    public GO m_targetParent;
    public GO m_targetOriginal;
    private Vector2 m_targetXYspeed;

    public GO m_tracker;
    public GO m_trackerParent;
    public GO m_trackerOriginal;

    public Network()
    {
        m_control = new Control();

        m_targetParent = new GO(GameObject.Find("[GekoList]"));
        m_targetOriginal = new GO(GameObject.Find("Geko"));
        m_target = new GO(GameObject.Instantiate(m_targetOriginal.getGO().transform, m_targetParent.getGO().transform).gameObject);
        m_target.getGO().transform.localPosition = new Vector3(0f, 0f, 0f);
        m_targetBody = m_target.getRigidbody2D();

        m_trackerParent = new GO(GameObject.Find("[TrackerList]"));
        m_trackerOriginal = new GO(GameObject.Find("Tracker"));
        m_tracker = new GO(GameObject.Instantiate(m_trackerOriginal.getGO().transform, m_trackerParent.getGO().transform).gameObject);
        m_tracker.getGO().GetComponent<TrackerClass>().m_target = m_target;
        m_tracker.getGO().transform.localPosition = new Vector3(0f, 0f, 0f);

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
        m_control.setKeys();

        m_targetXYspeed = m_targetBody.velocity;

        if (m_control.m_left)
        {
            m_targetXYspeed.x = -5;
            m_targetBody.velocity = m_targetXYspeed;
        }
        if (m_control.m_right)
        {
            m_targetXYspeed.x = 5;
            m_targetBody.velocity = m_targetXYspeed;
        }
        if (m_control.m_up)
        {

        }
        m_control.resetKeys();
    }
}
