#
# PySNMP MIB module GWTT-SMI (http://snmplabs.com/pysmi)
# ASN.1 source GWTT-SMI
# Source digest sha256:e1f28363dd0746f87c3c37ce24abe04ab43434a2534b247d96dee64357a51c90
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, enterprises, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "enterprises", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
gwtt = MibIdentifier((1, 3, 6, 1, 4, 1, 10072))
chips = MibIdentifier((1, 3, 6, 1, 4, 1, 10072, 1))
devices = MibIdentifier((1, 3, 6, 1, 4, 1, 10072, 2))
cards = MibIdentifier((1, 3, 6, 1, 4, 1, 10072, 3))
snmpProxy = MibIdentifier((1, 3, 6, 1, 4, 1, 10072, 4))
mibBuilder.exportSymbols("GWTT-SMI", cards=cards, chips=chips, devices=devices, gwtt=gwtt, snmpProxy=snmpProxy)
