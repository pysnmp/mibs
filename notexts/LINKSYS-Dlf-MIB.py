#
# PySNMP MIB module LINKSYS-Dlf-MIB (http://snmplabs.com/pysmi)
# ASN.1 source LINKSYS-Dlf-MIB
# Source digest sha256:1a6c53c12b1575567cf7c1a9076d1896c9cfc26fe970c109a7b01cc55617aec3
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("LINKSYS-MIB", "rnd")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rlDlf = ModuleIdentity((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 135))
if mibBuilder.loadTexts: rlDlf.setLastUpdated('2008-09-15 12:34')
if mibBuilder.loadTexts: rlDlf.setOrganization('Linksys LLC.')
rlDlfPortList = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 135, 1), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDlfPortList.setStatus('current')
mibBuilder.exportSymbols("LINKSYS-Dlf-MIB", PYSNMP_MODULE_ID=rlDlf, rlDlf=rlDlf, rlDlfPortList=rlDlfPortList)
