using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BlocPop
{
    public uint m_nbBlocX;
    public uint m_nbBloxY;
    public uint m_nbBloc;

    public List<Bloc> m_BlocList;

    public BlocPop()
    {
        m_nbBlocX = 3;
        m_nbBloxY = 3;
        m_nbBloc = m_nbBlocX * m_nbBloxY;

        m_BlocList = new List<Bloc>();
        m_BlocList.Add(new Bloc());
    }

    public void update(Vector2 a_targetPos)
    {
        foreach (Bloc b in m_BlocList)
        {
            b.update(a_targetPos);
        }
    }
}

public class Bloc
{
    public uint m_blocW;
    public uint m_blocH;
    public int m_value;

    public Bloc()
    {
        m_blocW = 10;
        m_blocH = 10;
        m_value = 0;
    }

    public void update(Vector2 a_targetPos)
    {

    }
}