from pydantic import BaseModel, Field, field_validator, conint, ConfigDict
from datetime import datetime
from dateutil.parser import parse
from typing import Optional, Union

class TremPassageirosModel(BaseModel):
    No: int = Field(..., description="Número da linha de registro")
    Open_Time: datetime = Field(..., description="Data e hora de abertura no formato datetime")
    Closed_Time: datetime = Field(..., description="Data e hora de fechamento no formato datetime")
    Line_ID: int = Field(..., description="Identificador da linha")
    Train_ID: int = Field(..., description="Identificador do trem")
    StartStation_ID: int = Field(..., description="ID da estação inicial")
    Station_ID: int = Field(..., description="ID da estação atual")
    NextStation_ID: int = Field(..., description="ID da próxima estação")
    EndStation_ID: int = Field(..., description="ID da estação final")
    Carriage_ID: int = Field(..., description="ID do vagão")
    Door_ID: int = Field(..., description="ID da porta")
    IN: int = Field(..., description="Número de passageiros que entraram")
    OUT: int = Field(..., description="Número de passageiros que saíram")
    Command: int = Field(..., description="Comando")
    SensorSts: int = Field(..., description="Status do sensor")
    filename: str = Field(..., description="Nome do arquivo associado")
    Door_Open_Duration: Optional[float] = Field(None, description="Duração da abertura da porta")
    Hour: Optional[int] = Field(None, ge=0, le=23, description="Hora em formato numérico (0-23)")
    Time_Interval: Optional[str] = Field(None, description="Intervalo de tempo (categoria)")
    Day_of_Week: Optional[int] = Field(None, ge=0, le=6, description="Dia da semana em formato numérico (0-6, onde 0 é domingo)")
    
    @field_validator('Open_Time', 'Closed_Time', mode='before')
    def parse_datetime(cls, value):
        """
        Remove espaços em branco e converte para datetime.
        """
        if isinstance(value, str):
            value = value.strip()  # Remove espaços ao redor
            return datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
        return value
    
    model_config = ConfigDict(arbitrary_types_allowed=True)

class IntervalosDiaModel(BaseModel):
    dt_hora_minuto: datetime
    day_of_week: str
    data_ingestao: Optional[datetime] = Field(None, description="Data de ingestão dos dados")
    data_linha: Optional[datetime] = Field(None, description="Data da linha")
    data_tag: Optional[datetime] = Field(None, description="Data da tag")

class EstacaoModel(BaseModel):
    id_estacao: int = Field(..., description="Identificador único da estação")
    tx_prefixo: str = Field(..., description="Prefixo da estação")
    tx_nome: str = Field(..., description="Nome da estação")
    cd_estacao_bu: int = Field(..., description="Código da estação no sistema BU")
    cluster: int = Field(..., description="Cluster ao qual a estação pertence")

class MovPeriodoModel(BaseModel):
    id_dt_hora_minuto: int = Field(..., description="Identificador único do período")
    cod_bilh: int = Field(..., description="Código do bilhete")
    cd_estac_bu: int = Field(..., description="Código da estação no sistema BU")
    dt_validacao: datetime = Field(..., description="Data e hora da validação do bilhete")
    total_validacoes: int = Field(..., description="Total de validações do bilhete")
    tipo_dia: str = Field(..., description="Tipo de dia (D para dia útil, F para fim de semana, etc.)")

    @field_validator("dt_validacao", mode='before')
    def parse_dt_validacao(cls, value: Union[str, datetime]):
        """Valida e transforma o campo `dt_validacao` em datetime se for uma string."""
        if isinstance(value, str):
            try:
                return parse(value)
            except ValueError:
                raise ValueError(f"Data inválida para 'dt_validacao': '{value}'. Formato esperado: ISO ou similar.")
        return value

    model_config = ConfigDict(arbitrary_types_allowed=True)

class TipoEmbarqueModel(BaseModel):
    cd_tipo_embarque: int = Field(..., description="Código do tipo de embarque")
    tx_movimento: str = Field(..., description="Descrição do movimento de embarque")
    cod_bilh: int = Field(..., description="Código do bilhete")
    cd_tipo_lancamento_fk: int = Field(..., description="Código de referência do lançamento")
    tx_lancamento: str = Field(..., description="Descrição do tipo de lançamento")

class DataIngestionModel(BaseModel):
    data_ingestao: int = Field(..., description="Timestamp da ingestão dos dados")
    data_linha: str = Field(..., description="Dados da linha, armazenados como JSON")
    data_tag: str = Field(..., description="Identificador da origem dos dados (nome do arquivo ou tabela)")
