#
# PySNMP MIB module MCAFEE-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mcafee/MCAFEE-SMI
# Produced by pysmi-1.1.12 at Wed Jul  3 12:25:42 2024
# On host fv-az1022-995 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, Counter32, Gauge32, Integer32, TimeTicks, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, Counter64, MibIdentifier, iso, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Counter32", "Gauge32", "Integer32", "TimeTicks", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "Counter64", "MibIdentifier", "iso", "ModuleIdentity", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mcafee = ModuleIdentity((1, 3, 6, 1, 4, 1, 1230))
mcafee.setRevisions(('2006-09-19 00:00',))
if mibBuilder.loadTexts: mcafee.setLastUpdated('200607110000Z')
if mibBuilder.loadTexts: mcafee.setOrganization('McAfee, Inc.')
mcafeeGATEWAY = ObjectIdentity((1, 3, 6, 1, 4, 1, 1230, 2))
if mibBuilder.loadTexts: mcafeeGATEWAY.setStatus('current')
mibBuilder.exportSymbols("MCAFEE-SMI", mcafeeGATEWAY=mcafeeGATEWAY, mcafee=mcafee, PYSNMP_MODULE_ID=mcafee)
