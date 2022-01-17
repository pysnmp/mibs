#
# PySNMP MIB module BEGEMOT-MIB2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/BEGEMOT-MIB2-MIB
# Produced by pysmi-1.1.8 at Mon Jan 17 21:48:05 2022
# On host fv-az33-58 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
begemotIp, = mibBuilder.importSymbols("BEGEMOT-IP-MIB", "begemotIp")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, ObjectIdentity, Counter64, ModuleIdentity, Bits, iso, Integer32, NotificationType, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "Counter64", "ModuleIdentity", "Bits", "iso", "Integer32", "NotificationType", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
begemotMib2 = ModuleIdentity((1, 3, 6, 1, 4, 1, 12325, 1, 3, 1))
begemotMib2.setRevisions(('2009-08-03 00:00', '2006-02-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: begemotMib2.setRevisionsDescriptions(('Second edition adds begemotIfDataPoll object.', 'Initial revision.',))
if mibBuilder.loadTexts: begemotMib2.setLastUpdated('200908030000Z')
if mibBuilder.loadTexts: begemotMib2.setOrganization('German Aerospace Center')
if mibBuilder.loadTexts: begemotMib2.setContactInfo('\t\tHartmut Brandt\n\n\t     Postal:\tGerman Aerospace Center\n\t\t\tOberpfaffenhofen\n\t\t\t82234 Wessling\n\t\t\tGermany\n\n\t     Fax:\t+49 8153 28 2843\n\n\t     E-mail:\tharti@freebsd.org')
if mibBuilder.loadTexts: begemotMib2.setDescription('The MIB for private mib2 stuff.')
begemotIfMaxspeed = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 3, 1, 1), Counter64()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotIfMaxspeed.setStatus('current')
if mibBuilder.loadTexts: begemotIfMaxspeed.setDescription('The speed of the fastest interface in ifTable in bps.')
begemotIfPoll = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 3, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotIfPoll.setStatus('current')
if mibBuilder.loadTexts: begemotIfPoll.setDescription('The current polling rate for the HC 64-bit counters.')
begemotIfForcePoll = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 3, 1, 3), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotIfForcePoll.setStatus('current')
if mibBuilder.loadTexts: begemotIfForcePoll.setDescription('The polling rate to be enforced for the HC 64-bit counters.\n\t     If this value is 0 the mib2 module computes a polling rate\n\t     depending on the value of begemotIfMaxspeed. If this value\n\t     turns out to be wrong, the polling rate can be force to an\n\t     arbitrary value by setting begemotIfForcePoll to a non-0\n\t     value. This may be necessary if an interface announces a wrong\n\t     bit rate in its MIB.')
begemotIfDataPoll = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 3, 1, 4), TimeTicks().clone(100)).setUnits('deciseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotIfDataPoll.setStatus('current')
if mibBuilder.loadTexts: begemotIfDataPoll.setDescription('The rate at which the mib2 module will poll interface data.')
mibBuilder.exportSymbols("BEGEMOT-MIB2-MIB", PYSNMP_MODULE_ID=begemotMib2, begemotIfForcePoll=begemotIfForcePoll, begemotIfPoll=begemotIfPoll, begemotIfMaxspeed=begemotIfMaxspeed, begemotIfDataPoll=begemotIfDataPoll, begemotMib2=begemotMib2)
