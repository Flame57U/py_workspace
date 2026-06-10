import time
import psycopg

PG_DIRECT = {
    "host": "127.0.0.1",
    "port": 5432,
    "dbname": "postgres",
    "user": "postgres",
    "password": "Sitp123123",
}

PG_BOUNCER = {
    "host": "127.0.0.1",
    "port": 6432,
    "dbname": "postgres",
    "user": "postgres",
    "password": "Sitp123123",
}


def check_connection(label: str, params: dict) -> None:
    print(f"\n{'='*40}")
    print(f"  {label}")
    print(f"  {params['host']}:{params['port']}")
    print(f"{'='*40}")
    try:
        t0 = time.perf_counter()
        with psycopg.connect(**params) as conn:
            elapsed = (time.perf_counter() - t0) * 1000
            with conn.cursor() as cur:
                cur.execute("SELECT version();")
                version = cur.fetchone()[0]
                cur.execute(
                    "SELECT count(*) FROM pg_stat_activity WHERE state = 'active';"
                )
                active = cur.fetchone()[0]
        print(f"  连接耗时 : {elapsed:.1f} ms")
        print(f"  PG 版本  : {version.split(',')[0]}")
        print(f"  活跃连接 : {active}")
        print(f"  状态     : OK")
    except Exception as e:
        print(f"  状态     : FAILED")
        print(f"  错误     : {e}")


if __name__ == "__main__":
    check_connection("直连 PostgreSQL :5432", PG_DIRECT)
    check_connection("经由 PgBouncer :6432", PG_BOUNCER)
    print()
