#
# PySNMP MIB module SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source SYSTEM-MIB
# Source digest sha256:c5fc65f4dd2d3098c1406d6e654d6324d6ca93ce71003c2d3503cc56a4cfde31
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, enterprises, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "enterprises", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
alcatel = MibIdentifier((1, 3, 6, 1, 4, 1, 637))
asd = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 61))
asam = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 61, 1))
ant = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 61, 2))
mibBuilder.exportSymbols("SYSTEM-MIB", alcatel=alcatel, ant=ant, asam=asam, asd=asd)
