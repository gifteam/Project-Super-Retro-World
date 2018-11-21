using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NetworkPop
{
    public int m_pop;
    public List<Network> m_Networklist;
    public bool m_alive;
    public List<double> m_fitness;
    public List<List<List<double>>> m_dna;

    public NetworkPop(int a_pop)
    {
        m_dna = new List<List<List<double>>>();
        m_fitness = new List<double>();
        m_Networklist = new List<Network>();
        m_pop = a_pop;
        m_alive = true;
        for (int i_popIndex = 0; i_popIndex < m_pop; i_popIndex++)
        {
            m_Networklist.Add(new Network(i_popIndex));
            m_fitness.Add(0.0);
        }
        foreach (Network n in m_Networklist)
        {
            n.ghostGekos();
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

    public void getDna()
    {
        m_dna.Clear();
        foreach (Network n in m_Networklist)
        {
            n.getDna();
            m_dna.Add(n.m_dna);
        }
    }
}

public class Network
{
    public int m_index;
    public double m_fitness;
    public List<Perceptron> m_PerceptronList;
    public BlocPop m_blocPop;
    public Control m_control;
    public List<List<double>> m_dna;

    public GO m_target;
    public Rigidbody2D m_targetBody;
    public GO m_targetParent;
    public GO m_targetOriginal;
    private Vector2 m_targetXYspeed;

    private int m_targetJmpTimer = 0;
    private int m_targetJmpForce = 350;
    public float m_targetDistToGround;
    private LayerMask m_groundLayer;

    public GO m_tracker;
    public GO m_trackerParent;
    public GO m_trackerOriginal;

    public bool m_alive;

    public Network(int a_index)
    {
        m_index = a_index;
        m_dna = new List<List<double>>();
        m_control = new Control();
        m_alive = true;

        m_targetParent = new GO(GameObject.Find("[GekoList]"));
        m_targetOriginal = new GO(GameObject.Find("Geko"));
        m_target = new GO(GameObject.Instantiate(m_targetOriginal.getGO().transform, m_targetParent.getGO().transform).gameObject);
        m_target.getGO().transform.localPosition = new Vector3(0f, 0f, 0f);
        m_targetBody = m_target.getRigidbody2D();

        m_groundLayer = LayerMask.GetMask("Ground");
        m_targetDistToGround = m_target.getBoxCollider2D().bounds.extents.y + 0.2f;


        m_trackerParent = new GO(GameObject.Find("[TrackerList]"));
        m_trackerOriginal = new GO(GameObject.Find("Tracker"));
        m_tracker = new GO(GameObject.Instantiate(m_trackerOriginal.getGO().transform, m_trackerParent.getGO().transform).gameObject);
        m_tracker.getGO().GetComponent<TrackerClass>().m_target = m_target;
        m_tracker.getGO().transform.localPosition = new Vector3(0f, 0f, 0f);

        m_blocPop = new BlocPop(m_target);
        m_PerceptronList = new List<Perceptron>();
        m_fitness = 0;
        uint l_pop = 4; 
        for (uint i_popIndex = 0; i_popIndex < l_pop; i_popIndex++)
        {
            m_PerceptronList.Add(new Perceptron(m_blocPop, m_control));
        }
    }

    public void setWeigth(int a_perceptronIndex, Perceptron a_parentPerceptron)
    {
        m_PerceptronList[a_perceptronIndex].setWeigth(a_parentPerceptron);
    }

    public void getDna()
    {
        m_dna.Clear();
        foreach (Perceptron p in m_PerceptronList)
        {
            p.getDnaPart();
            m_dna.Add(p.m_dnaPart);
        }
    }

    public void ghostGekos()
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
            m_control.activationFunction();
            m_control.setKeys();

            m_targetXYspeed = m_targetBody.velocity;

            if (m_control.m_left == true)
            {
                m_targetXYspeed.x = -5;
                m_targetBody.velocity = m_targetXYspeed;
            }
            if (m_control.m_right == true)
            {
                m_targetXYspeed.x = 5;
                m_targetBody.velocity = m_targetXYspeed;
            }
            if (m_control.m_up == true && m_targetJmpTimer == 0)
            {
                m_targetJmpTimer = 100;
                if (m_target.isGrounded(ref m_targetDistToGround, ref m_groundLayer))
                {
                    m_targetBody.AddForce(Vector2.up * m_targetJmpForce);
                }
            }
            if (m_targetJmpTimer > 0)
            {
                m_targetJmpTimer--;
            }
            m_control.resetKeys();
        }
    }
}
