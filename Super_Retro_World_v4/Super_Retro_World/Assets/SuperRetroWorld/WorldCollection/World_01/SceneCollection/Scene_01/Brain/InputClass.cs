using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BlocPop
{
    public int m_nbBlocX;
    public int m_nbBloxY;
    public int m_nbBloc;
    public GO m_target;

    public List<Bloc> m_BlocList;

    public BlocPop(GO a_target)
    {
        m_target = a_target;
        m_nbBloc = 16;

        m_BlocList = new List<Bloc>();

        for (int i_blocIndex = 0; i_blocIndex < m_nbBloc; i_blocIndex++)
        {
            float l_deltaX = Mathf.Cos((float)i_blocIndex * Mathf.PI / 8) * 3.0f; ;
            float l_deltaY = Mathf.Sin((float)i_blocIndex * Mathf.PI / 8) * 3.0f; ;
            m_BlocList.Add(new Bloc(m_target, l_deltaX, l_deltaY));
        }
    }

    public void update()
    {
        foreach (Bloc b in m_BlocList)
        {
            b.update();
        }
    }
}

public class Bloc
{
    public int m_value;
    public GO m_go;
    public InputColliderClass m_goScript;
    public GO m_goOrigin;
    public GO m_parent;
    public Vector2 m_blocPos;

    public Bloc(GO a_parent, float a_deltaX, float a_deltaY)
    {
        m_parent = a_parent;
        m_goOrigin = new GO(GameObject.Find("InputBloc"));
        m_go = new GO(GameObject.Instantiate(m_goOrigin.getGO().transform, m_parent.getGO().transform).gameObject);
        m_goScript = m_go.getGO().GetComponent<InputColliderClass>();

        m_blocPos = new Vector2(a_deltaX, a_deltaY);
        m_go.setLocalPos(m_blocPos);
        m_value = 0;
    }

    public void update()
    {
        if (m_go.getGO() ?? false)
        {
            m_go.setLocalPos(m_blocPos);
            m_value = m_goScript.m_value;
        }
    }
}