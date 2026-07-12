import type { ColumnDef } from './DataTable'

export interface Employee extends Record<string, unknown> {
  id: number
  name: string
  department: string
  role: string
  salary: number
  startDate: string
  status: 'Active' | 'On Leave' | 'Terminated'
}

export const employees: Employee[] = [
  { id: 1,  name: 'Alice Hartman',     department: 'Engineering', role: 'Senior Engineer',       salary: 132000, startDate: '2019-03-12', status: 'Active'     },
  { id: 2,  name: 'Brian Kowalski',    department: 'Marketing',   role: 'Marketing Manager',     salary: 98000,  startDate: '2020-07-01', status: 'Active'     },
  { id: 3,  name: 'Carmen Vega',       department: 'Sales',       role: 'Account Executive',     salary: 87000,  startDate: '2021-01-15', status: 'Active'     },
  { id: 4,  name: 'David Chen',        department: 'Finance',     role: 'Financial Analyst',     salary: 91000,  startDate: '2018-11-03', status: 'Active'     },
  { id: 5,  name: 'Elena Petrov',      department: 'HR',          role: 'HR Business Partner',   salary: 82000,  startDate: '2022-02-28', status: 'Active'     },
  { id: 6,  name: 'Frank Oduya',       department: 'Design',      role: 'UX Designer',           salary: 105000, startDate: '2020-09-14', status: 'Active'     },
  { id: 7,  name: 'Grace Liu',         department: 'Engineering', role: 'Staff Engineer',        salary: 158000, startDate: '2017-06-20', status: 'Active'     },
  { id: 8,  name: 'Henry Mbeki',       department: 'Sales',       role: 'Sales Director',        salary: 140000, startDate: '2016-04-11', status: 'Active'     },
  { id: 9,  name: 'Isla Novak',        department: 'Marketing',   role: 'Content Strategist',    salary: 78000,  startDate: '2023-01-09', status: 'Active'     },
  { id: 10, name: 'James Okafor',      department: 'Engineering', role: 'Junior Engineer',       salary: 85000,  startDate: '2023-06-05', status: 'Active'     },
  { id: 11, name: 'Keiko Tanaka',      department: 'Finance',     role: 'Controller',            salary: 125000, startDate: '2019-08-22', status: 'Active'     },
  { id: 12, name: 'Luis Romero',       department: 'Design',      role: 'Brand Designer',        salary: 92000,  startDate: '2021-03-30', status: 'On Leave'   },
  { id: 13, name: 'Megan Frost',       department: 'HR',          role: 'Recruiter',             salary: 71000,  startDate: '2022-11-01', status: 'Active'     },
  { id: 14, name: 'Nathan Park',       department: 'Engineering', role: 'DevOps Engineer',       salary: 118000, startDate: '2020-05-17', status: 'Active'     },
  { id: 15, name: 'Olivia Grant',      department: 'Sales',       role: 'Account Executive',     salary: 84000,  startDate: '2021-09-08', status: 'Active'     },
  { id: 16, name: 'Pablo Reyes',       department: 'Marketing',   role: 'SEO Specialist',        salary: 74000,  startDate: '2022-04-19', status: 'Active'     },
  { id: 17, name: 'Quinn Adler',       department: 'Engineering', role: 'Senior Engineer',       salary: 135000, startDate: '2018-12-03', status: 'Active'     },
  { id: 18, name: 'Rachel Kim',        department: 'Finance',     role: 'FP&A Manager',          salary: 112000, startDate: '2019-02-14', status: 'Active'     },
  { id: 19, name: 'Samuel Torres',     department: 'Design',      role: 'Product Designer',      salary: 108000, startDate: '2020-10-27', status: 'On Leave'   },
  { id: 20, name: 'Tanya Osei',        department: 'Sales',       role: 'Sales Manager',         salary: 118000, startDate: '2018-07-02', status: 'Active'     },
  { id: 21, name: 'Uma Patel',         department: 'Engineering', role: 'Machine Learning Eng',  salary: 148000, startDate: '2021-05-10', status: 'Active'     },
  { id: 22, name: 'Victor Hale',       department: 'HR',          role: 'HR Director',           salary: 130000, startDate: '2015-03-31', status: 'Active'     },
  { id: 23, name: 'Wendy Larsson',     department: 'Marketing',   role: 'Brand Manager',         salary: 95000,  startDate: '2020-01-22', status: 'Active'     },
  { id: 24, name: 'Xavier Dupont',     department: 'Engineering', role: 'Security Engineer',     salary: 139000, startDate: '2019-07-16', status: 'Active'     },
  { id: 25, name: 'Yuki Yamamoto',     department: 'Design',      role: 'Motion Designer',       salary: 89000,  startDate: '2022-08-04', status: 'Active'     },
  { id: 26, name: 'Zoe Wallace',       department: 'Finance',     role: 'Staff Accountant',      salary: 68000,  startDate: '2023-02-13', status: 'Active'     },
  { id: 27, name: 'Aaron Singh',       department: 'Engineering', role: 'Engineering Manager',   salary: 162000, startDate: '2016-09-29', status: 'Active'     },
  { id: 28, name: 'Bella Cruz',        department: 'Sales',       role: 'Business Dev Rep',      salary: 72000,  startDate: '2023-04-03', status: 'Active'     },
  { id: 29, name: 'Carlos Mendez',     department: 'Marketing',   role: 'Demand Gen Manager',    salary: 102000, startDate: '2020-11-18', status: 'Active'     },
  { id: 30, name: 'Diana Nwosu',       department: 'HR',          role: 'HRIS Analyst',          salary: 79000,  startDate: '2021-06-07', status: 'Active'     },
  { id: 31, name: 'Ethan Brandt',      department: 'Engineering', role: 'Frontend Engineer',     salary: 115000, startDate: '2020-03-23', status: 'Active'     },
  { id: 32, name: 'Fiona Mackay',      department: 'Design',      role: 'Design Lead',           salary: 122000, startDate: '2018-05-14', status: 'Active'     },
  { id: 33, name: 'George Adeyemi',    department: 'Sales',       role: 'Enterprise AE',         salary: 145000, startDate: '2017-10-05', status: 'Active'     },
  { id: 34, name: 'Hannah Beck',       department: 'Finance',     role: 'Senior Analyst',        salary: 104000, startDate: '2019-12-01', status: 'On Leave'   },
  { id: 35, name: 'Ivan Kozlov',       department: 'Engineering', role: 'Backend Engineer',      salary: 122000, startDate: '2020-08-10', status: 'Active'     },
  { id: 36, name: 'Julia Santos',      department: 'Marketing',   role: 'Social Media Manager',  salary: 76000,  startDate: '2022-05-25', status: 'Active'     },
  { id: 37, name: 'Kevin Okonkwo',     department: 'Engineering', role: 'Platform Engineer',     salary: 128000, startDate: '2019-04-17', status: 'Active'     },
  { id: 38, name: 'Laura Johansson',   department: 'HR',          role: 'L&D Specialist',        salary: 77000,  startDate: '2021-10-12', status: 'Active'     },
  { id: 39, name: 'Marcus Webb',       department: 'Sales',       role: 'SDR Manager',           salary: 97000,  startDate: '2020-06-29', status: 'Active'     },
  { id: 40, name: 'Nina Hoffman',      department: 'Design',      role: 'UX Researcher',         salary: 98000,  startDate: '2021-02-08', status: 'Active'     },
  { id: 41, name: 'Oscar Lindqvist',   department: 'Finance',     role: 'Treasury Analyst',      salary: 88000,  startDate: '2020-09-03', status: 'Active'     },
  { id: 42, name: 'Priya Sharma',      department: 'Engineering', role: 'Data Engineer',         salary: 131000, startDate: '2020-12-14', status: 'Active'     },
  { id: 43, name: 'Roberto Fiore',     department: 'Marketing',   role: 'Product Marketing Mgr', salary: 108000, startDate: '2019-05-21', status: 'Terminated' },
  { id: 44, name: 'Sophie Müller',     department: 'Sales',       role: 'Account Executive',     salary: 86000,  startDate: '2022-01-17', status: 'Active'     },
  { id: 45, name: 'Thomas Eriksson',   department: 'Engineering', role: 'QA Engineer',           salary: 95000,  startDate: '2021-07-26', status: 'Active'     },
  { id: 46, name: 'Ursula Bauer',      department: 'HR',          role: 'Compensation Analyst',  salary: 84000,  startDate: '2020-04-06', status: 'Active'     },
  { id: 47, name: 'Vincent Leroy',     department: 'Design',      role: 'Design Systems Eng',    salary: 118000, startDate: '2020-02-24', status: 'Active'     },
  { id: 48, name: 'Wanda Kowalczyk',   department: 'Finance',     role: 'Payroll Manager',       salary: 94000,  startDate: '2018-09-09', status: 'Active'     },
  { id: 49, name: 'Xander Rousseau',   department: 'Engineering', role: 'Infrastructure Eng',    salary: 126000, startDate: '2019-10-30', status: 'Active'     },
  { id: 50, name: 'Yasmin Khalil',     department: 'Marketing',   role: 'Email Marketing Spec',  salary: 72000,  startDate: '2023-03-06', status: 'Active'     },
  { id: 51, name: 'Zachary Moore',     department: 'Sales',       role: 'Sales Operations',      salary: 88000,  startDate: '2021-08-19', status: 'Active'     },
  { id: 52, name: 'Amara Diallo',      department: 'Engineering', role: 'Embedded Engineer',     salary: 119000, startDate: '2020-07-15', status: 'Active'     },
  { id: 53, name: 'Boris Volkov',      department: 'Finance',     role: 'Risk Analyst',          salary: 97000,  startDate: '2019-01-28', status: 'Active'     },
  { id: 54, name: 'Chloe Dubois',      department: 'Design',      role: 'Visual Designer',       salary: 85000,  startDate: '2022-07-11', status: 'Active'     },
  { id: 55, name: 'Derek Washington',  department: 'Sales',       role: 'Regional VP Sales',     salary: 178000, startDate: '2014-11-17', status: 'Active'     },
  { id: 56, name: 'Erin Nakamura',     department: 'HR',          role: 'Employee Relations',    salary: 80000,  startDate: '2022-09-20', status: 'Active'     },
  { id: 57, name: 'Felix Gruber',      department: 'Engineering', role: 'Site Reliability Eng',  salary: 142000, startDate: '2018-03-07', status: 'Active'     },
  { id: 58, name: 'Gabriela Ruiz',     department: 'Marketing',   role: 'Growth Analyst',        salary: 83000,  startDate: '2022-06-13', status: 'Active'     },
  { id: 59, name: 'Hugo Fischer',      department: 'Finance',     role: 'CFO',                   salary: 245000, startDate: '2013-08-01', status: 'Active'     },
  { id: 60, name: 'Ingrid Svensson',   department: 'Design',      role: 'Creative Director',     salary: 155000, startDate: '2015-05-18', status: 'Active'     },
  { id: 61, name: 'Julian Moreau',     department: 'Engineering', role: 'Software Architect',    salary: 168000, startDate: '2016-02-09', status: 'Active'     },
  { id: 62, name: 'Kira Petersen',     department: 'Sales',       role: 'Customer Success Mgr',  salary: 94000,  startDate: '2021-04-14', status: 'Active'     },
  { id: 63, name: 'Liam O\'Brien',     department: 'Engineering', role: 'Mobile Engineer',       salary: 121000, startDate: '2020-10-01', status: 'Active'     },
  { id: 64, name: 'Mia Bergmann',      department: 'HR',          role: 'Talent Acquisition Lead',salary: 93000, startDate: '2019-09-25', status: 'Active'     },
  { id: 65, name: 'Noah Andersson',    department: 'Marketing',   role: 'VP Marketing',          salary: 185000, startDate: '2015-12-07', status: 'Active'     },
  { id: 66, name: 'Olivia Schmitt',    department: 'Finance',     role: 'Internal Auditor',      salary: 99000,  startDate: '2020-06-16', status: 'Active'     },
  { id: 67, name: 'Peter Novotny',     department: 'Engineering', role: 'CTO',                   salary: 280000, startDate: '2012-04-23', status: 'Active'     },
  { id: 68, name: 'Rosa Delgado',      department: 'Design',      role: 'Illustrator',           salary: 78000,  startDate: '2022-10-03', status: 'Active'     },
  { id: 69, name: 'Stefan Braun',      department: 'Sales',       role: 'Partnerships Manager',  salary: 106000, startDate: '2020-08-28', status: 'Terminated' },
  { id: 70, name: 'Tina Huang',        department: 'Engineering', role: 'Fullstack Engineer',    salary: 117000, startDate: '2021-11-22', status: 'Active'     },
  { id: 71, name: 'Ulrich Weber',      department: 'Finance',     role: 'Senior Accountant',     salary: 86000,  startDate: '2021-03-15', status: 'Active'     },
  { id: 72, name: 'Vera Sorokina',     department: 'Marketing',   role: 'Analytics Manager',     salary: 107000, startDate: '2020-02-03', status: 'Active'     },
  { id: 73, name: 'William Carter',    department: 'HR',          role: 'Chief People Officer',  salary: 210000, startDate: '2013-06-30', status: 'Active'     },
  { id: 74, name: 'Xenia Popov',       department: 'Engineering', role: 'AI Engineer',           salary: 155000, startDate: '2022-03-21', status: 'Active'     },
  { id: 75, name: 'Yusuf Al-Rashid',   department: 'Sales',       role: 'Mid-Market AE',         salary: 96000,  startDate: '2021-12-06', status: 'Active'     },
]

export const columns: ColumnDef<Employee>[] = [
  {
    key: 'id',
    header: 'ID',
    sortable: true,
  },
  {
    key: 'name',
    header: 'Name',
    sortable: true,
  },
  {
    key: 'department',
    header: 'Department',
    sortable: true,
  },
  {
    key: 'role',
    header: 'Role',
    sortable: true,
  },
  {
    key: 'salary',
    header: 'Salary',
    sortable: true,
    render: (value) => {
      const num = value as number
      return new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD', maximumFractionDigits: 0 }).format(num)
    },
  },
  {
    key: 'startDate',
    header: 'Start Date',
    sortable: true,
    render: (value) => {
      const dateStr = value as string
      return new Date(dateStr).toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' })
    },
  },
  {
    key: 'status',
    header: 'Status',
    sortable: true,
    render: (value) => {
      const status = value as Employee['status']
      const colors: Record<Employee['status'], string> = {
        'Active':     '#16a34a',
        'On Leave':   '#d97706',
        'Terminated': '#dc2626',
      }
      return (
        <span style={{ color: colors[status], fontWeight: 600 }}>
          {status}
        </span>
      )
    },
  },
]
