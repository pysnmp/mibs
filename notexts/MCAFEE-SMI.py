#
# PySNMP MIB module MCAFEE-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mcafee/MCAFEE-SMI
# Produced by pysmi-1.1.8 at Thu Feb  9 12:04:53 2023
# On host fv-az173-80 platform Linux version 5.15.0-1031-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, iso, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, ObjectIdentity, NotificationType, enterprises, Bits, Unsigned32, MibIdentifier, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "ObjectIdentity", "NotificationType", "enterprises", "Bits", "Unsigned32", "MibIdentifier", "Counter32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mcafee = ModuleIdentity((1, 3, 6, 1, 4, 1, 1230))
mcafee.setRevisions(('2006-09-19 00:00',))
if mibBuilder.loadTexts: mcafee.setLastUpdated('200607110000Z')
if mibBuilder.loadTexts: mcafee.setOrganization('McAfee, Inc.')
mcafeeGATEWAY = ObjectIdentity((1, 3, 6, 1, 4, 1, 1230, 2))
if mibBuilder.loadTexts: mcafeeGATEWAY.setStatus('current')
mibBuilder.exportSymbols("MCAFEE-SMI", mcafee=mcafee, PYSNMP_MODULE_ID=mcafee, mcafeeGATEWAY=mcafeeGATEWAY)
