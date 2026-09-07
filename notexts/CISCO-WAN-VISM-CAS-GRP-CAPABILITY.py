#
# PySNMP MIB module CISCO-WAN-VISM-CAS-GRP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-WAN-VISM-CAS-GRP-CAPABILITY
# Source digest sha256:42e9b4e6a8da2c52400ea47aa7064894f51982184d046c735fb64545c530f8b7
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWanVismCasGrpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 333))
if mibBuilder.loadTexts: ciscoWanVismCasGrpCapability.setLastUpdated('2000-12-05 00:00')
if mibBuilder.loadTexts: ciscoWanVismCasGrpCapability.setOrganization('Cisco Systems, Inc.')
cwvismCasGrpCapability1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 333, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwvismCasGrpCapability1 = cwvismCasGrpCapability1.setProductRelease('VISM Release 2.1.0 and MGX-8850 Release 1.1.34')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwvismCasGrpCapability1 = cwvismCasGrpCapability1.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-VISM-CAS-GRP-CAPABILITY", PYSNMP_MODULE_ID=ciscoWanVismCasGrpCapability, ciscoWanVismCasGrpCapability=ciscoWanVismCasGrpCapability, cwvismCasGrpCapability1=cwvismCasGrpCapability1)
