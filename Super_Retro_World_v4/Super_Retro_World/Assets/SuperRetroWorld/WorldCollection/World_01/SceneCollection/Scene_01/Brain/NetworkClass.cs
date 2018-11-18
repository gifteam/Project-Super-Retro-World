using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NetworkPop
{
    public int m_pop;
    public List<Network> m_Networklist;
    public bool m_alive;
    public List<double> m_fitness;

    public NetworkPop(int a_pop)
    {
        m_fitness = new List<double>();
        m_Networklist = new List<Network>();
        m_pop = a_pop;
        m_alive = true;
        for (uint i_popIndex = 0; i_popIndex < m_pop; i_popIndex++)
        {
            m_Networklist.Add(new Network());
            m_fitness.Add(0.0);
        }
        foreach (Network n in m_Networklist)
        {
            n.ghostInputs();
        }
    }

    public void update()
    {
        m_alive = false;
        int l_nIndex = 0;
        foreach (Network n in m_Networklist)
        {
            n.update();
            m_fitness[l_nIndex] = n.m_fitness;
            l_nIndex++;
            if (n.m_alive)
            {
                m_alive = true;
            }
        }
    }
}

public class Network
{
    public double m_fitness;
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

    public bool m_alive;

    public Network()
    {
        m_control = new Control();
        m_alive = true;

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

    public void ghostInputs()
    {
        GameObject[] m_goTargetList = GameObject.FindGameObjectsWithTag("Geko");
        BoxCollider2D l_collider1 = m_target.getBoxCollider2D();
        BoxCollider2D l_collider2;
        foreach (GameObject l_otherTarget in m_goTargetList)
        {
            l_collider2 = l_otherTarget.GetComponent<BoxCollider2D>();
            Physics2D.IgnoreCollision(l_collider1, l_collider2, true);
        }
    }

    public void update()
    {
        if (m_target.getGO() ?? false)
        {
            m_alive = true;
        }else
        {
            m_alive = false;
        }

        if (m_alive)
        {
            m_fitness += 0.1;
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
}
